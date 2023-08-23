output "ssh_access_command" {
  description = "The access command to EC2 instance with public IP"
  value       = "ssh -i ${var.key_pair_name}.pem ec2-user@${module.ec2_instance.public_ip}"
}