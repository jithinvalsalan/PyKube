from kubernetes import client, config
from columnar import columnar

config.load_kube_config()

v1 = client.CoreV1Api()
def list_all_pods():
    print("Listing pods with their IPs")
    ret = v1.list_pod_for_all_namespaces(watch=False)

    data = []
    headers = ['NAMESPACE','POD IP','HOST IP','NODE NAME','POD NAME']
    for i in ret.items:
        #print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (i.metadata.namespace, i.status.pod_ip,  i.status.host_ip, i.spec.node_name,  i.metadata.name ))
        data1 = [i.metadata.namespace, i.status.pod_ip,  i.status.host_ip, i.spec.node_name, i.metadata.name]
        data1 = data.append(data1)
        table = columnar(data,headers,no_borders=False,wrap_max=0)
        csv = columnar(data,headers,no_borders=True,wrap_max=0)
        fo=open("ListingPods.csv",'w')
        fo.write(csv)
        fo.close()
    print(table)
    #print (csv)

list_all_pods()