---
layout: page
title: "RBAC"
permalink: /rbac
nav_order: 3
---
# Securing Namespaces with RBAC
## Create 2 namespaces and associated resources

```
kubectl apply -f exercice-files/lab2-1.yaml
```
![](assets/images/rbac/create.png)

## Check access with existing kubeconfig

```
kubectl get pods -A -l 'run=test'
```
![](assets/images/rbac/display.png)

## Create demo RBAC

```
kubectl apply -f exercice-files/lab2-2.yaml
```

![](assets/images/rbac/apply.png)

## Update kubeconfig

```
cat<<EOF>>.kube/config
- name: dev-ns1
  user:
    token: $(kubectl get secret dev-ns1-token -n ns1 -ojsonpath="{.data.token}" | base64 -d)
EOF
```

![](assets/images/rbac/token.png)

```
kubectl config set-context 'dev-ns1@handson-k8s-cluster' --cluster='handson-k8s-cluster' --namespace='ns1' --user='dev-ns1'
```

![](assets/images/rbac/context.png)

## Check access with created access

```
kubectl config use-context 'dev-ns1@handson-k8s-cluster'
```

![](assets/images/rbac/switch.png)

```
kubectl get pods -A -l 'run=test'
```

![](assets/images/rbac/deny-all.png)

```
kubectl get pods -n ns2 -l 'run=test'
```

![](assets/images/rbac/deny-ns2.png)

```
kubectl get pods,svc
```

![](assets/images/rbac/allow-ns1.png)

```
kubectl logs test-ns1
```

![](assets/images/rbac/allow-logs.png)

```
kubectl exec test-ns1 -- /bin/sh
```

![](assets/images/rbac/deny-exec.png)

## Switch back to admin kubeconfig

```
kubectl config use-context 'admin@handson-k8s-cluster'
```

![](assets/images/rbac/back.png)
