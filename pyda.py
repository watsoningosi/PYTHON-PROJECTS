import wolframalpha

Client = wolframalpha.client("Y76R37-VPE9P28TK4")

res = Client.query('temperature in Washington, DC on October 3, 2012')

print(res)

