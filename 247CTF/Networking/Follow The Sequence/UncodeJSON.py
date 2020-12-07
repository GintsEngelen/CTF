import json


with open("CombinedFilter", "r") as pcap:
    JSONdata = pcap.read()
data = json.loads(JSONdata)

print(type(data))

payloadList = []

for element in data:
    seqNo = int(element['_source']['layers']['tcp']['tcp.options_tree']['mptcp']['tcp.options.mptcp.rawdataseqno'])
    if 'tcp.payload' in element['_source']['layers']['tcp']:
        payLoad = bytes.fromhex(element['_source']['layers']['tcp']['tcp.payload'].replace(':', ''))
        payloadList.append((seqNo, payLoad))

payloadList.sort()

with open("alldata", "wb") as writeout:
    for element in payloadList:
        writeout.write(element[1])

with open("alldata", "rb") as filehandle:
    with open("truncated", "wb") as writebinary:
        writebinary.write(filehandle.read()[0xf4:])