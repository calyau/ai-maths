---
concept: Positive Semi-definite Form
slug: positive-semi-definite-form
category: bilinear-forms
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.2 Symmetric Forms"
extraction_confidence: high
aliases: ["positive semidefinite"]
prerequisites: [symmetric-bilinear-form]
extends: [symmetric-bilinear-form]
related: [positive-definite-form]
contrasts_with: [positive-definite-form]
answers_questions: ["What is a positive semi-definite form?"]
---
# Quick Definition
A symmetric form is positive semi-definite if (v, v) >= 0 for all nonzero vectors v. Unlike positive definite forms, (v, v) = 0 is allowed for nonzero v.
# Core Definition
A symmetric form on a real vector space is positive semi-definite if (v, v) >= 0 for all nonzero vectors v (Artin, p. 242).
# Prerequisites
- **Symmetric bilinear form** — Positive semi-definiteness is a property of symmetric forms
# Key Properties
1. (v, v) >= 0 for all v
2. May have (v, v) = 0 for nonzero v (unlike positive definite)
3. May be degenerate
4. All eigenvalues of the matrix are >= 0
# Examples
**Example 1**: The form on R^2 with matrix [[1, 0],[0, 0]] is positive semi-definite but not positive definite.
# Relationships
## Related
- **Positive definite form** — Stricter: requires (v,v) > 0 for nonzero v
## Contrasts With
- **Positive definite form** — Semi-definite allows (v,v) = 0
# Source Reference
Chapter 8: Bilinear Forms, Section 8.2, page 242.
# Verification Notes
- Definition source: Direct from p. 242
- Confidence rationale: Briefly defined alongside positive definite
- Uncertainties: None
- Cross-reference status: Verified
