from diagrams import Cluster, Diagram, Edge
from diagrams.onprem import ci, cd, gitops, container, vcs
from diagrams.gcp import devtools
from diagrams.saas import chat
from diagrams.k8s import controlplane

with Diagram("CICD", filename="img/cicd", show=False):
    with Cluster("CI"):
        git = vcs.Git("Source Repository")
        actions = ci.GithubActions("Github Actions")
        docker = container.Docker("Docker")
        gcr = devtools.ContainerRegistry("Container Registry")
        CISlack = chat.Slack("CI Slack")
        git >> actions >> docker >> gcr
        actions \
            - Edge(label="alert", style="dashed") \
            >> CISlack

    with Cluster("CD"):
        argocd = gitops.Argocd("Argocd")
        gitopsRepo = vcs.Git("GitOps Repository")
        k8sControlPlane = controlplane.API("Controleplane")
        CDSlack = chat.Slack("CD Slack")
        actions >> gitopsRepo << argocd >> k8sControlPlane
        argocd \
            - Edge(label="alert", style="dashed") \
            >> CDSlack

