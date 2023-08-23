# Configurar un nuevo perfil
aws configure --profile juan-hurtado-cloudcamp

ingresar
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=

exportar el perfil
export AWS_PROFILE=juan-hurtado-cloudcamp

# Configuracion de contexto de Cluster
## Descargar contexto de cluster EKS de AWS
```sh
aws eks update-kubeconfig --region us-east-1 --name {cluster_name} --kubeconfig {file_name}

aws eks update-kubeconfig --region us-east-1 --name eks-juan-hurtado --kubeconfig eks-juan-hurtado-config
```

## Mover archivo a carpeta .kube

* Agregar extension .yaml al archivo descargado

```sh
cp eks-juan-hurtado-config /Users/juanhz0101/.kube
```