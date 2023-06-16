---
layout: page
title: "Application Metrics"
permalink: /metrics
nav_order: 9
---
# Bonus Stage: Application Metrics
## Deploy demo application

```
kubectl apply -f exercice-files/lab9-1.yaml
```

![](assets/images/metrics/create.png)

## Query Metrics endpoint

```
kubectl run -i --rm --restart=Never --image=busybox:latest shell -- wget -qO- http://test-metrics:9001
```

![](assets/images/metrics/test.png)

## Apply prometheus agent manifest

Generate a token to push metrics

![](assets/images/metrics/tok1.png)

![](assets/images/metrics/tok2.png)

![](assets/images/metrics/tok3.png)

Fill the token in manifest

```
sed -i 's/COCKPIT/{YOUR TOKEN}/g' exercice-files/lab9-2.yaml
```

![](assets/images/metrics/tok4.png)

```
kubectl apply -f exercice-files/lab9-2.yaml
```

![](assets/images/metrics/apply.png)

## Check cockpit for metrics

Login using a new grafana user

![](assets/images/metrics/graf1.png)

![](assets/images/metrics/graf2.png)

![](assets/images/metrics/graf3.png)

![](assets/images/metrics/graf4.png)

Search for metrics

![](assets/images/metrics/metrics.png)

