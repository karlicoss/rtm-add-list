* sudo vim /usr/local/lib/python3.5/dist-packages/rtm/rtm.py 
   comment warning. call

version 2 to make subtasks work
     params['api_key'] = self.apiKey
     params['format'] = 'json'
     params['v'] = '2'
     params['api_sig'] = self._sign(params)

