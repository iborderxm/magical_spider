from runflow import magical_start,magical_request,magical_close

project_name = '药监局1'
base_url = 'http://www.lxspider.com'
request_list = [
   'http://www.lxspider.com/?p=486',
   'http://www.lxspider.com/?p=743'
]

session_id, process_url = magical_start(project_name, base_url)

if session_id and process_url:
   for request_url in request_list:
       result = magical_request(session_id, process_url, request_url)
       if result:
           print(result)

   magical_close(session_id, process_url, project_name)
else:
   print("Error: Failed to create browser or select session_id.")