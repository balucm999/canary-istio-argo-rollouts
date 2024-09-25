note:
after insatlling argo rollout controller and plugin then 1st we have to apply namespace and gateway yaml which is present cd.. and goto single-svc-vs-multiple-set and aplly one by one and lastly we should apply rollout and
---imp---no need to maintain sepeare deployment yaml so instead of using deploymnet and rollout-for-deployment yaml use single rollout.yaml


#install argo rollout controller

kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml

note:---IMP----install argo rollouts controller in argo-rollouts namespace only

----------------------------------------

#Install argorollout plugin for kubectl

wget https://github.com/argoproj/argo-rollouts/releases/download/v1.7.2/kubectl-argo-rollouts-linux-amd64

chmod +x kubectl-argo-rollouts-linux-amd64


sudo mv kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts

kubectl argo rollouts version

kubectl get pods -n istio-argo-rollouts

vi rollout.yaml (change image and set weight)
kubectl apply -f rollout.yaml

kubectl argo rollouts get rollout rollouts-demo -n istio-argo-rollouts -w

kubectl describe vs -n istio-argo-rollouts

kubectl argo rollouts promote rollouts-demo -n istio-argo-rollouts

kubectl argo rollouts get rollout rollouts-demo -n istio-argo-rollouts -w


kubectl argo rollouts undo rollouts-demo -n istio-argo-rollouts

kubectl argo rollouts get rollout rollouts-demo -n istio-argo-rollouts -w
