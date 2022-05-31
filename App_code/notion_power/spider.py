import operator

from mitmproxy import ctx


def response(flow):
    # 响应的状态码

    if operator.contains(flow.request.url, 'index/getChangeBid'):
        # with open('user.txt','w') as fp:
        #     fp.write(flow.response.text)
        ctx.log.error(str(flow.response.text))
        
