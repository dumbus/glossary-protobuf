from concurrent import futures

import logging
import grpc

from .generated import glossary_pb2
from .generated import glossary_pb2_grpc

class GlossaryService(glossary_pb2_grpc.GlossaryServiceServicer):
  def __init__(self):
    self.data = {
        'fps': glossary_pb2.Term(
          title='fps',
          definition='Количество сменяемых на интерфейсе кадров за одну секунду.',
          source_link='https://developer.mozilla.org/ru/docs/Glossary/FPS'
        ),
        'fcp': glossary_pb2.Term(
          title='fcp',
          definition='Время, за которое пользователь увидит какое-то содержимое веб-страницы, например, текст или картинку.',
          source_link='https://developer.mozilla.org/ru/docs/Glossary/First_contentful_paint'
        ),
        'fid': glossary_pb2.Term(
          title='fid',
          definition='Время ожидания до первого взаимодействия с контентом.',
          source_link='https://habr.com/ru/companies/timeweb/articles/714280/'
        ),
        'tbt': glossary_pb2.Term(
          title='tbt',
          definition='Общее количество времени, когда основной поток заблокирован достаточно долго, чтобы реагировать на взаимодействия пользователя.',
          source_link='https://habr.com/ru/companies/domclick/articles/549098/'
        ),
        'cls': glossary_pb2.Term(
          title='cls',
          definition='Какое количество содержимого во viewport двигалось во время загрузки страницы.',
          source_link='https://habr.com/ru/companies/domclick/articles/549098/'
        ),
      }


  def GetAllTerms(self, request, context):
    return glossary_pb2.GetAllTermsResponse(terms=self.data)


  def GetTerm(self, request, context):
    keyword = request.keyword

    if keyword not in self.data:
      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details(f"Термин '{keyword}' не найден")
      return glossary_pb2.TermResponse()
    
    return glossary_pb2.TermResponse(term=self.data[keyword])


  def CreateTerm(self, request, context):
    keyword = request.keyword
    term = request.term
    
    if keyword in self.data:
      context.set_code(grpc.StatusCode.ALREADY_EXISTS)
      context.set_details(f"Термин '{keyword}' уже существует")
      return glossary_pb2.TermResponse()
    
    self.data[keyword] = term
    return glossary_pb2.TermResponse(term=term)


  def UpdateTerm(self, request, context):
    keyword = request.keyword
    
    if keyword not in self.data:
      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details(f"Термин '{keyword}' не найден")
      return glossary_pb2.TermResponse()

    term = self.data[keyword]
    
    if request.definition:
      term.definition = request.definition
    if request.source_link:
      term.source_link = request.source_link
    
    return glossary_pb2.TermResponse(term=term)


  def DeleteTerm(self, request, context):
    keyword = request.keyword
    
    if keyword not in self.data:
      context.set_code(grpc.StatusCode.NOT_FOUND)
      context.set_details(f"Термин '{keyword}' не найден")
      return glossary_pb2.TermResponse()
    
    deleted_term = self.data.pop(keyword)
    return glossary_pb2.TermResponse(term=deleted_term)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

  glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(GlossaryService(), server)

  server.add_insecure_port('[::]:50051')
  server.start()

  print("Glossary Server started on port 50051")
  
  server.wait_for_termination()

if __name__ == '__main__':
  logging.basicConfig()
  serve()