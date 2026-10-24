# Synthetic SOP: Payment Status Inquiry

## Scope
This fictional procedure describes a read-only check for a payment status inquiry in the sample PolicyAdmin application.

## Preconditions
Confirm the support request is authorized and identify the synthetic transaction reference in the approved system. Do not request or expose full payment credentials.

## Procedure
1. Open the approved support console.
2. Search using the authorized transaction reference.
3. Check the current status and the last update timestamp.
4. If the status is pending, follow the documented reconciliation window.
5. If the status is failed, capture the approved error code and route according to the incident matrix.

## Restrictions
This procedure is read-only. Do not retry payments, change policy records, or modify financial data based on an AI-generated recommendation.

## Verification
Confirm the status directly in the source system before drafting a response.
