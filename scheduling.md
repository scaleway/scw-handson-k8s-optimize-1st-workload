---
layout: page
title: "Scheduling"
permalink: /scheduling
nav_order: 4
---
# Scheduling pods - affinity pattern
## Check node labels

```
kubectl get nodes --show-labels
```

![](assets/images/scheduling/labels.png)


## Create new deployment without affinity

```
kubectl apply -f exercice-files/lab4-1.yaml
```

![](assets/images/scheduling/create.png)

## Check pods location

```
kubectl get pods -ocustom-columns=NAME:.metadata.name,NODE:.spec.nodeName
```

![](assets/images/scheduling/check.png)

## Recreate deployment with affinity

```
kubectl replace -f exercice-files/lab4-2.yaml
```

![](assets/images/scheduling/replace.png)

## Check pods location

```
kubectl get pods -ocustom-columns=NAME:.metadata.name,NODE:.spec.nodeName
```

![](assets/images/scheduling/affinity.png)


## Clean up

```
kubectl delete -f exercice-files/lab4-2.yaml
```

![](assets/images/scheduling/cleanup.png)

To go further check [the official documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
