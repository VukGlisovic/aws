# EC2


Here we will explain how to create an instance and how you can connect
to the instance with ssh. The explanations are based on
<a href="https://docs.aws.amazon.com/vpc/latest/userguide/getting-started-ipv4.html">Getting Started with IPv4 for Amazon VPC</a>.
The steps below are more of a summary compared to the AWS tutorial. 

In short, the steps are:
1. create a virtual private cloud (VPC)
2. create public subnet within the VPC
3. create security group and add rules for your instance
4. launch instance into the subnet
5. associate Elastic Ip address to your instance
6. connect to your instance
7. clean up


### 1.&2. Create your VPC and subnet
In the AWS console, go to `VPC` under `Services` (note in the top right
the region you are in). Click `Launch VPC Wizard`. You can leave the
defaults, but, fill in a name for the VPC and the public subnet.


### 3. Create security group and add rules
To associate a security group with an instance, you specify the
security group when you launch the instance. To create a security
group, go to `VPC` under `Services` and click `Security Groups`.
Now create your new security group. Select the VPC you created in
the previous step and then create the security group. Now add the
following rules to the `Inbound Rules`:
* HTTP with 0.0.0.0/0 in the `Source` field. Allows inbound HTTP
access from any IPv4 address.
* HTTPS with 0.0.0.0/0 in the `Source` field. Allows inbound HTTPS
access from any IPv4 address.
* SSH with either your networks public ip address range or 0.0.0.0/0
to enable all ip addresses and open port 22.


### 4. Launch an instance
Make sure you are still in the same region as where you create your
VPC. Go to `EC2` under `Services`. Click `Launch Instance`. Follow
the wizard and make sure you specify your VPC, your subnet and your
security group. Finally, either create a new key pair or use an existing
one to be able to connect to the instance later on.


### 5. Associate elastic IP address to your instance
In order to connect to the instance, our instance needs a public IPv4
address to be able to communicate with the internet. Here you will
allocate an elastic ip address to your account. Go to `VPC` under
`Services` and navigate to `Elastic IPs`. Choose `Allocate new address`
and then `Allocate`. Select the newly allocated ip address, choose
`Actions` and then `Associate Address`. Here you can select the instance
you launched in the previous step, to associate the elastic ip address
with.


### 6. Connect to your instance
Use ssh to connect to your instance. You have to specify the path to the
private key and the user_name@public_dns_name. For example, if you used
Amazon Linux 2 or the Amazon Linux AMI, the user name is ec2-user.
```bash
ssh -i /path/my-key-pair.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
```
Instead of using the public dns name, you could also use the elastic IP
address directly (the public dns name resolves to the public IP address
or the elastic IP address).

If you stuble upon the following problem: `WARNING: UNPROTECTED PRIVATE
KEY FILE!`,
then you have to change permissions on the keyfile with `chmod 600` (no
read and write access for non-root users).


### 7. Clean up
To prevent making additional costs, remove:
* the EC2 instance
* the VPC (automatically deletes subnets associated with it and
security groups and more)
* the elastic IP address
