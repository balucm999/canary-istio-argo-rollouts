#install argo rollout controller
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-rollouts/stable/manifests/install.yaml

#Install argorollout plugin for kubectl


wget https://github.com/argoproj/argo-rollouts/releases/download/v1.7.2/kubectl-argo-rollouts-linux-amd64

chmod +x kubectl-argo-rollouts-linux-amd64


sudo mv kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts


kubectl argo rollouts version

kubectl argo rollouts get rollout rollouts-demo -n istio-argo-rollouts -w
