variable "vpc_id" {
  description = "The ID of the VPC"
  type        = string
  default = "vpc-056866ef3c275c9bf"
}

variable "subnet_id" {
  description = "The ID of the subnet"
  type        = string
  default = "subnet-010b888d1b0f03443"
}

variable "key_pair_name" {
  description = "The name of the key pair to attach to the instance"
  type        = string
  default = "j.hurtadokp"
}

variable "instance_name" {
  description = "The name of the instance"
  type        = string
  default = "jenkins-server-juan-hurtado"
}

variable "resource_owner" {
  description = "The name of the resource owner in tags"
  type        = string
  default = "juan-pablo-hurtado"
}

variable "my_public_ip" {
  description = "The public personal IP"
  type        = string
  default = "177.254.16.207/32"
}


