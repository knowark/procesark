base = {
    # --- PROVIDERS ---
    "QueryParser": {
        "method": "query_parser"
    },
    "TenantProvider": {
        "method": "standard_tenant_provider"
    },
    "AuthProvider": {
        "method": "standard_auth_provider"
    },
    # --- REPOSITORIES ---
    "ProcessRepository": {
        "method": "memory_process_repository"
    },
    "JobRepository": {
        "method": "memory_job_repository"
    },
    "AllocationRepository": {
        "method": "memory_allocation_repository"
    },
    "TriggerRepository": {
        "method": "memory_trigger_repository"
    },
    "RunRepository": {
        "method": "memory_run_repository"
    },
    # --- SERVICES ---
    "Scheduler": {
        "method": "standard_scheduler"
    },
    "Executor": {
        "method": "memory_executor"
    },
    # --- COORDINATORS ---
    "LaunchCoordinator": {
        "method": "launch_coordinator"
    },
    "StageCoordinator": {
        "method": "stage_coordinator"
    },
    "SessionCoordinator": {
        "method": "session_coordinator"
    },
    # --- INFORMERS ---
    "ProcesarkInformer": {
        "method": "standard_procesark_informer"
    },
    # --- SUPPLIERS ---
    "TenantSupplier": {
        "method": "memory_tenant_supplier"
    }
}
