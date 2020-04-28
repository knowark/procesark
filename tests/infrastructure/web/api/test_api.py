from pytest import raises
from json import loads, dumps
from aiohttp import web


async def test_root(app) -> None:
    response = await app.get('/')

    content = await response.text()

    assert response.status == 200
    assert 'Procesark' in content


async def test_root_api(app) -> None:
    response = await app.get('/?api')
    data = await response.text()
    api = loads(data)

    assert 'openapi' in api
    assert api['info']['title'] == 'Procesark'


# async def test_questionnaires_head(app, headers) -> None:
#     response = await app.head('/questionnaires', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 3


# async def test_questionnaires_get_unauthorized(app) -> None:
#     response = await app.get('/questionnaires')
#     content = await response.text()

#     assert response.status == 401
#     data_dict = loads(content)
#     assert 'error' in data_dict


# async def test_questionnaires_get(app, headers) -> None:
#     response = await app.get('/questionnaires', headers=headers)
#     content = await response.text()
#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 3
#     assert data_dict[0]['id'] == 'LMK123'


# async def test_questionnaires_get_route_filter(app, headers) -> None:
#     response = await app.get(
#         '/questionnaires?filter=[["name", "=", "Inspections"]]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1


# async def test_bad_filter_get_route_filter(app, headers) -> None:
#     response = await app.get('/questionnaires?filter=[[**BAD FILTER**]]',
#                              headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 3


# async def test_questionnaires_put(app, headers) -> None:
#     questionnaire_data = dumps([{
#         "id": "07506ce5-edd7-4eab-af9c-4e555bc8e098",
#         "name": "Cleansing Form",
#         "description": "Cleaning Management Questionnaire",
#         "questions": [
#             {
#                 "id": "5099f02b-9cfc-489b-bd6d-18b3263e518d",
#                 "name": "First Question",
#                 "type": "selection",
#                 "options": [
#                     {"name": "First Option"}
#                 ]
#             },
#             {
#                 "id": "635550e2-280f-4a84-9f93-992c2a7e4ba6",
#                 "name": "Second Question",
#                 "type": "text"
#             },
#             {
#                 "id": "9cec33fc-95c7-49fe-b35d-266cb578b778",
#                 "name": "Third Question",
#                 "type": "selection",
#                 "options": [
#                     {
#                         "id": "283650a2-4dc3-4914-9e74-0ae43ef6e1f6",
#                         "name": "Second Option"
#                     },
#                     {
#                         "id": "5ffcc875-7bc4-463d-b0bf-c34906857624",
#                         "name": "Third Option"
#                     },
#                     {
#                         "id": "b9ac29ae-0329-44e9-8435-34cce3aef58c",
#                         "name": "Fourth Option"
#                     }
#                 ]
#             }
#         ]
#     }])

#     response = await app.put('/questionnaires',
#                              data=questionnaire_data, headers=headers)
#     content = await response.text()
#     assert response.status == 200


# async def test_questionnaires_delete(app, headers) -> None:
#     response = await app.delete('/questionnaires/LMK123', headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/questionnaires', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 2


# async def test_questionnaires_delete_body(app, headers) -> None:
#     ids = dumps(["LMK123"])
#     response = await app.delete(
#         '/questionnaires', data=ids, headers=headers)
#     content = await response.text()
#     assert response.status == 204

#     response = await app.get('/questionnaires', headers=headers)
#     data_dict = loads(await response.text())

#     assert len(data_dict) == 2


# async def test_questions_get(app, headers) -> None:
#     response = await app.get('/questions', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 1
#     assert data_dict[0]['id'] == '001'


# async def test_questions_get_route_filter(app, headers) -> None:
#     response = await app.get(
#         '/questions?filter=[["questionnaireId", "=", "LMK123"]]',
#         headers=headers)
#     content = await response.text()
#     data_dict = loads(content)
#     assert len(data_dict) == 1


# async def test_questions_head(app, headers) -> None:
#     response = await app.head('/questions', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 1


# async def test_options_get(app, headers) -> None:
#     response = await app.get('/options', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 1
#     assert data_dict[0]['id'] == 'ABC'


# async def test_options_head(app, headers) -> None:
#     response = await app.head('/options', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 1


# async def test_assessments_head(app, headers) -> None:
#     response = await app.head('/assessments', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2


# async def test_assessments_get(app, headers) -> None:
#     response = await app.get('/assessments', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2
#     assert data_dict[0]['id'] == '001'


# async def test_assessments_put(app, headers) -> None:
#     assessment_data = dumps([{
#         'id': '07506ce5-edd7-4eab-af9c-4e555bc8e098',
#         'questionnaireId': '07506ce5-edd7-4eab-af9c-4e555bc8e098',
#         'answers': [
#             {
#                 'value': 'Answer for second question',
#                 'questionId': '635550e2-280f-4a84-9f93-992c2a7e4ba6'
#             },
#             {
#                 'questionId': '9cec33fc-95c7-49fe-b35d-266cb578b778',
#                 'optionIds': [
#                     "5ffcc875-7bc4-463d-b0bf-c34906857624",
#                     "b9ac29ae-0329-44e9-8435-34cce3aef58c"
#                 ]
#             },
#         ]}])

#     response = await app.put('/assessments', data=assessment_data,
#                              headers=headers)
#     content = await response.text()
#     assert response.status == 200

#     response = await app.head('/selections', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 2

#     response = await app.get('/selections', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 2


# async def test_answers_head(app, headers) -> None:
#     response = await app.head('/answers', headers=headers)
#     count = response.headers.get('Total-Count')

#     assert int(count) == 1


# async def test_answers_get(app, headers) -> None:
#     response = await app.get('/answers', headers=headers)
#     content = await response.text()

#     assert response.status == 200

#     data_dict = loads(content)

#     assert len(data_dict) == 1
#     assert data_dict[0]['id'] == '001'
