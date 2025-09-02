import subprocess

user = ''
password = ''
ip_start = '0.0.0'
ip_end = '0'

file = './cam_script_log'
with open(file) as content:
  last_logged_ip = content.read().strip()
  if last_logged_ip:
    ip_end = last_logged_ip

def open_cam(user, password, ip_start, num):
  command = 'ffplay'
  arg1 = '-an'
  arg2 = '-hide_banner' 
  arg3 = f'rtsp://{user}:{password}@{ip_start}.{num}:554/onvif1'
  result = subprocess.run([command, arg1, arg2, arg3], capture_output=True)
  return result

test_cam = str(open_cam(user, password, ip_start, ip_end).stderr)

if 'failed' in test_cam or 'Bad Request' in test_cam:
  for number in range(10,30):
    test_cam = str(open_cam(user, password, ip_start, number).stderr)
    if 'failed' not in test_cam and 'Bad Request' not in test_cam:
      with open(file, 'w') as last_logged_ip:
        last_logged_ip.write(str(number))
      break
