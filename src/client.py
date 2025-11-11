from __future__ import print_function

import grpc

from .generated import glossary_pb2
from .generated import glossary_pb2_grpc

def run():
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = glossary_pb2_grpc.GlossaryServiceStub(channel)
    

    print("--- Получение всех терминов ---")
    try:
      response = stub.GetAllTerms(glossary_pb2.GetAllTermsRequest())
      for keyword, term in response.terms.items():
        print(f"{keyword}: {term.title}")
        print(f"Определение: {term.definition}")
        if term.source_link:
          print(f"Источник: {term.source_link}")
        print()
    except grpc.RpcError as e:
      print(f"Ошибка: {e.details()}")
    
    print("\n\n")
    print("--- Получение одного термина - 'fps' ---")
    try:
      response = stub.GetTerm(glossary_pb2.GetTermRequest(keyword='fps'))
      print(f"Найден термин: {response.term.title}")
      print(f"Определение: {response.term.definition}")
    except grpc.RpcError as e:
      print(f"Ошибка: {e.details()}")
    

    print("\n\n")
    print("--- Создание нового термина ---")
    try:
      new_term = glossary_pb2.Term(
        title='lcp',
        definition='Largest Contentful Paint - метрика производительности веб-страниц',
        source_link='https://web.dev/lcp/'
      )
      response = stub.CreateTerm(glossary_pb2.CreateTermRequest(
        keyword='lcp', 
        term=new_term
      ))
      print(f"Создан термин: {response.term.title}")
    except grpc.RpcError as e:
      print(f"Ошибка: {e.details()}")
    

    print("\n\n")
    print("--- Обновление термина ---")
    try:
      response = stub.UpdateTerm(glossary_pb2.UpdateTermRequest(
        keyword='lcp',
        definition='Largest Contentful Paint - метрика производительности веб-страниц (ОБНОВЛЕНО)'
      ))
      print(f"Обновлен термин: {response.term.title}")
      print(f"Новое определение: {response.term.definition}")
    except grpc.RpcError as e:
      print(f"Ошибка: {e.details()}")
    

    print("\n\n")
    print("--- Удаление термина ---")
    try:
      response = stub.DeleteTerm(glossary_pb2.DeleteTermRequest(keyword='lcp'))
      print(f"Удален термин: {response.term.title}")
    except grpc.RpcError as e:
      print(f"Ошибка: {e.details()}")


if __name__ == '__main__':
  run()