---
layout: page
title: "Network policies"
permalink: /netpol
nav_order: 4
---
# Securing Namespaces with Network Policies
## Test existing connectivity

```
kubectl run -i --rm --restart=Never --image=busybox:latest -n ns1 shell -- wget -qO- http://test.ns2.svc.cluster.local
```

![](assets/images/netpol/allow.png)

## Apply demo network policy

```
kubectl apply -f exercice-files/lab3.yaml
```

![](assets/images/netpol/apply.png)

This demo policy has been built using a GUI available here: [https://editor.networkpolicy.io/](https://editor.networkpolicy.io/)

![](assets/images/netpol/gui.png)

## Test new connectivity

```
kubectl run -i --rm --restart=Never --image=busybox:latest -n ns1 shell -- wget -qO- http://test.ns1.svc.cluster.local
```

![](assets/images/netpol/ok.png)

```
kubectl run -i --rm --restart=Never --image=busybox:latest -n ns1 shell -- wget -qO- http://test.ns2.svc.cluster.local
```

![](assets/images/netpol/ko.png)
