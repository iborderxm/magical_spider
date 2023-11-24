import requests
sess = requests.session()
host = 'http://127.0.0.1:5000'

# 创建浏览器和选择会话ID
def magical_start(project_name, base_url='http://www.lxspider.com'):
  # 1、create browser and select session_id
  try:
      response = sess.post(f'{host}/create', data={'name': project_name, 'url': base_url})
      session_id = response.json()['session_id']
      process_url = response.json()['process_url']
  except Exception as e:
      print(f'Error in creating browser: {e}')
      return None, None

  return session_id, process_url


# 请求浏览器
def magical_request(session_id, process_url, request_url, request_type='get', formdata=''):
  # 2、request browser_xhr
  data = {'session_id': session_id, 'process_url': process_url,
          'request_url': request_url, 'request_type': request_type}

  if request_type.lower() == 'post':
      data.update({'request_type': 'post', 'formdata': formdata})

  try:
      response = sess.post(f'{host}/xhr', data=data)
      return response.json()['result']
  except Exception as e:
      print(f'Error in request browser: {e}')
      return None


# 关闭浏览器
def magical_close(session_id, process_url, process_name):
  # 4、close browser
  try:
      close_data = {'session_id': session_id, 'process_url': process_url, 'process_name': process_name}
      sess.post(f'{host}/close', data=close_data)
  except Exception as e:
      print(f'Error in closing browser: {e}')