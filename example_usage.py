from client import OpenModelRegistryLicenseComplianceAuditorClient

def main():
    client = OpenModelRegistryLicenseComplianceAuditorClient()
    res = client.audit_model_license('opencsg/open-code-pro-7b', 'FINANCIAL_PROPRIETARY_API')
    print('OpenCSG License Auditor: ' + res['license_audit_id'] + ' (' + res['declared_spdx_license'] + ')')
    print('Commercial Permitted: ' + str(res['commercial_redistribution_permitted']) + ' | Risk Score: ' + str(res['training_dataset_copyright_risk_score']))
    print('Status: ' + res['compliance_attestation_status'])
    print('Provenance URL: ' + res['registry_provenance_url'])

if __name__ == '__main__':
    main()
