out_fields = '''Protocol:,Prefix:,AD/Metric:,Next-Hop:,Last update:,OutboundInterface:'''
out_fields = out_fields.split(',')

with open("ospf.txt", "r") as ospf_route_file:
    for ospf_route in ospf_route_file:
        ospf_route = ospf_route.replace("O","OSPF")
        ospf_route = ospf_route.replace("[","")
        ospf_route = ospf_route.replace("]","")
        ospf_route = ospf_route.replace(",", "").split()
        ospf_route.remove('via')
        for i in range(len(ospf_route)):
            print(f'{out_fields[i]:18} {ospf_route[i]}')
