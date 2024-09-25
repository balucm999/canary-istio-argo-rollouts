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
