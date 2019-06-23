# Redshift


Here we'll briefly discuss the creation of a redshift cluster and 
connecting to a redshift cluster.

When creating a redshift cluster, you need to have a subnet group. You
can create one by navigating to `Amazon Redshift`, page `Security` and
tab `Subnet Groups`. Here you can select a subnet in a VPC of your
preference. Make sure the VPC can be publicly accessed and that there's
a security group associated with the VPC, that has access to Redshift.

In order to connect to a database you need:
1. server name/host
2. port
3. username
4. password

In notebook `redshift/01-introduction-redshift-client.ipynb`, you can
see how to connect to a redshift cluster, create data and query for
that data.
