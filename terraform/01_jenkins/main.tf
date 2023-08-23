provider "aws" {
  region = "us-east-1"
}

module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "5.2.1"
  vpc_security_group_ids = [aws_security_group.sg.id]
  subnet_id = var.subnet_id
  name               = var.instance_name
  ami                = "ami-0453898e98046c639"
  instance_type      = "t2.micro"
  key_name           = var.key_pair_name
  user_data = file("${path.module}/userdata.sh")
  associate_public_ip_address = true

  tags = {
    bootcamp = "devops"
    Name = var.instance_name
    Owner = var.resource_owner
  }
}

resource "aws_security_group" "sg" {
  name        = "allow_http"
  description = "Allow inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_public_ip]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = [var.my_public_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
