from django.urls import path

from extras.views import ObjectChangeLogView
from ipam.views import ServiceCreateView
from . import views
from .models import Cluster, ClusterGroup, ClusterType, VirtualMachine

app_name = 'virtualization'
urlpatterns = [

    # Cluster types
    path('cluster-types/', views.ClusterTypeListView.as_view(), name='clustertype_list'),
    path('cluster-types/add/', views.ClusterTypeCreateView.as_view(), name='clustertype_add'),
    path('cluster-types/import/', views.ClusterTypeBulkImportView.as_view(), name='clustertype_import'),
    path('cluster-types/delete/', views.ClusterTypeBulkDeleteView.as_view(), name='clustertype_bulk_delete'),
    path('cluster-types/<slug:slug>/edit/', views.ClusterTypeEditView.as_view(), name='clustertype_edit'),
    path('cluster-types/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='clustertype_changelog', kwargs={'model': ClusterType}),

    # Cluster groups
    path('cluster-groups/', views.ClusterGroupListView.as_view(), name='clustergroup_list'),
    path('cluster-groups/add/', views.ClusterGroupCreateView.as_view(), name='clustergroup_add'),
    path('cluster-groups/import/', views.ClusterGroupBulkImportView.as_view(), name='clustergroup_import'),
    path('cluster-groups/delete/', views.ClusterGroupBulkDeleteView.as_view(), name='clustergroup_bulk_delete'),
    path('cluster-groups/<slug:slug>/edit/', views.ClusterGroupEditView.as_view(), name='clustergroup_edit'),
    path('cluster-groups/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='clustergroup_changelog', kwargs={'model': ClusterGroup}),

    # Clusters
    path('clusters/', views.ClusterListView.as_view(), name='cluster_list'),
    path('clusters/add/', views.ClusterCreateView.as_view(), name='cluster_add'),
    path('clusters/import/', views.ClusterBulkImportView.as_view(), name='cluster_import'),
    path('clusters/edit/', views.ClusterBulkEditView.as_view(), name='cluster_bulk_edit'),
    path('clusters/delete/', views.ClusterBulkDeleteView.as_view(), name='cluster_bulk_delete'),
    path('clusters/<int:pk>/', views.ClusterView.as_view(), name='cluster'),
    path('clusters/<int:pk>/edit/', views.ClusterEditView.as_view(), name='cluster_edit'),
    path('clusters/<int:pk>/delete/', views.ClusterDeleteView.as_view(), name='cluster_delete'),
    path('clusters/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='cluster_changelog', kwargs={'model': Cluster}),
    path('clusters/<int:pk>/devices/add/', views.ClusterAddDevicesView.as_view(), name='cluster_add_devices'),
    path('clusters/<int:pk>/devices/remove/', views.ClusterRemoveDevicesView.as_view(), name='cluster_remove_devices'),

    # Virtual machines
    path('virtual-machines/', views.VirtualMachineListView.as_view(), name='virtualmachine_list'),
    path('virtual-machines/add/', views.VirtualMachineCreateView.as_view(), name='virtualmachine_add'),
    path('virtual-machines/import/', views.VirtualMachineBulkImportView.as_view(), name='virtualmachine_import'),
    path('virtual-machines/edit/', views.VirtualMachineBulkEditView.as_view(), name='virtualmachine_bulk_edit'),
    path('virtual-machines/delete/', views.VirtualMachineBulkDeleteView.as_view(), name='virtualmachine_bulk_delete'),
    path('virtual-machines/<int:pk>/', views.VirtualMachineView.as_view(), name='virtualmachine'),
    path('virtual-machines/<int:pk>/edit/', views.VirtualMachineEditView.as_view(), name='virtualmachine_edit'),
    path('virtual-machines/<int:pk>/delete/', views.VirtualMachineDeleteView.as_view(), name='virtualmachine_delete'),
    path('virtual-machines/<int:pk>/config-context/', views.VirtualMachineConfigContextView.as_view(), name='virtualmachine_configcontext'),
    path('virtual-machines/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='virtualmachine_changelog', kwargs={'model': VirtualMachine}),
    path('virtual-machines/<int:virtualmachine>/services/assign/', ServiceCreateView.as_view(), name='virtualmachine_service_assign'),

    # VM interfaces
    path('interfaces/add/', views.InterfaceCreateView.as_view(), name='interface_add'),
    path('interfaces/edit/', views.InterfaceBulkEditView.as_view(), name='interface_bulk_edit'),
    path('interfaces/delete/', views.InterfaceBulkDeleteView.as_view(), name='interface_bulk_delete'),
    path('interfaces/<int:pk>/edit/', views.InterfaceEditView.as_view(), name='interface_edit'),
    path('interfaces/<int:pk>/delete/', views.InterfaceDeleteView.as_view(), name='interface_delete'),
    path('virtual-machines/interfaces/add/', views.VirtualMachineBulkAddInterfaceView.as_view(), name='virtualmachine_bulk_add_interface'),

]
