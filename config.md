---
layout: page
title: "ConfigMap and Secret"
permalink: /config
nav_order: 7
---
# ConfigMap and Secret
## Create configmap and secret

```
kubectl apply -f exercice-files/lab7-1.yaml
```

![](assets/images/config/create1.png)

## Create same deployment in both namespace

```
kubectl apply -n ns1 -f exercice-files/lab7-2.yaml
```

```
kubectl apply -n ns2 -f exercice-files/lab7-2.yaml
```

![](asset/images/config/create2.png)

## Check applications

```
kubectl get pod -A -l app=test-cm-sec
```

![](asset/images/config/pod.png)

```
kubectl exec -n {NAMESPACE} -i {POD NAME} -- wget -qO- http://127.0.0.1
```

![](asset/images/config/ok.png)

## Cleanup

```
kubectl delete -f exercice-files/lab7-1.yaml
```

(Deleting a namespace trigger deletion of its resource)
