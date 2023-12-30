from diagrams import Cluster, Diagram
from diagrams.gcp import compute, network, database, security

with Diagram("GCP", filename="img/gcp", show=False):
    with Cluster("Public"):
        with Cluster("Network"):
            dns = network.DNS("Cloud DNS")
            certMap = security.SecurityCommandCenter("Certificate Map")
            lb = network.LoadBalancing("Network Load Balancer")
            dns >> certMap >> lb

    with Cluster("VPC"):
        vpc = network.VPC("VPC")
        with Cluster("Workloads"):
            gke = compute.GKE("GKE")
            gce = compute.GCE("Compute Engine")
        db = database.SQL("Postgres DB")
        lb >> vpc
        vpc >> gke >> gce >> db