import json,sys,subprocess
U='https://ekfechanion.eu/wp-json/elementor/mcp/'
def post(body,sid=None):
    h=['-H','Content-Type: application/json','-H','Accept: application/json, text/event-stream']
    if sid: h+=['-H',f'Mcp-Session-Id: {sid}']
    r=subprocess.run(['curl','-sS','-D','-','-X','POST',U,*h,'--data-binary','@-'],input=json.dumps(body).encode(),capture_output=True)
    out=r.stdout.decode(); 
    hdr,_,b=out.rpartition('\r\n\r\n')
    s=[l.split(':',1)[1].strip() for l in hdr.split('\r\n') if l.lower().startswith('mcp-session-id')]
    return (s[0] if s else sid), b
def call(name,args):
    sid,_=post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"cli","version":"1"}}})
    post({"jsonrpc":"2.0","method":"notifications/initialized"},sid)
    _,b=post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}},sid)
    return b
if __name__=='__main__':
    if sys.argv[1]=='list':
        sid,_=post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"cli","version":"1"}}})
        _,b=post({"jsonrpc":"2.0","id":2,"method":"tools/list"},sid)
        print([t['name'] for t in json.loads(b)['result']['tools']])
    else:
        print(call(sys.argv[1],json.load(open(sys.argv[2])))[:3000])
