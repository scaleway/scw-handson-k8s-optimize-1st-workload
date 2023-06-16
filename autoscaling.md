---
layout: page
title: "Autoscaling"
permalink: /autoscaling
nav_order: 5
---
# Autoscaling pods and nodes
## Create a deployment with associated HPA

```
kubectl apply -f exercice-files/lab5-1.yaml
```

![](assets/images/autoscaling/create.png)

## Trigger load on deployment

```
kubectl apply -f exercice-files/lab5-2.yaml
```

![](assets/images/autoscaling/load.png)

## Observe HPA

```
kubectl get hpa test -w
```

![](assets/images/autoscaling/hpa-load.png)

Exit with `Ctrl+C`

```
kubectl get pods
```

![](assets/images/autoscaling/pod.png)

## Increase load

```
kubectl scale --replicas=2 deploy load-generator
```

![](assets/images/autoscaling/scale.png)

## Observe cluster autoscaling

```
kubectl get pods
```

![](assets/images/autoscaling/pod2.png)

In the Scaleway Console, check Kapsule cluster pools

![](assets/images/autoscaling/nodes.png)

## Clean up

```
kubectl delete -f exercice-files/lab5-1.yaml -f exercice-files/lab5-2.yaml
```

![](assets/images/autoscaling/cleanup.png)

## Trigger job on specific pool

```
kubectl create -f exercice-files/lab5-3.yaml
```

![](assets/images/autoscaling/job.png)

## Observe cluster autoscaling

```
kubectl get job,pods -l job=test
```

![](assets/images/autoscaling/job2.png)

In the Scaleway Console, check Kapsule cluster pools

![](assets/images/autoscaling/nodes2.png)

## Clean up

```
kubectl delete job -l job=test
```

![](assets/images/autoscaling/cleanup2.png)
