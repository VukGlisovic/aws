# EC2

Here we will explain how to create an instance and how you can connect
to the instance with ssh. The explanations are based on
<a href="https://docs.aws.amazon.com/vpc/latest/userguide/getting-started-ipv4.html">Getting Started with IPv4 for Amazon VPC</a>.
The steps below are more of a summary compared to the AWS tutorial. 

In short, the steps are:
1. create a virtual private cloud (VPC)
2. create public subnet within the VPC
3. create security group for your instance
4. launch instance into the subnet
5. associate Elastic Ip address to your instance
6. connect to your instance
7. clean up


### 1.&2. create your VPC and subnet
In the AWS console, go to `VPC` under `Services` (note in the top right
the region you are in). Click `Launch VPC Wizard`. You can leave the
defaults, but, fill in a name for the VPC and the public subnet.


### 3. create security group
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


### 4. launch an instance
Make sure you are still in the same region as where you create your
VPC. Go to `EC2` under `Services`. Click `Launch Instance`. Follow
the wizard and make sure you specify your VPC, your subnet and your
security group. Finally, either create a new key pair or use an existing
one to be able to connect to the instance later on.

