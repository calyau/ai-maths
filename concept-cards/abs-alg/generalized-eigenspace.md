---
concept: Generalized Eigenspace
slug: generalized-eigenspace
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 491
section: "12.3 The Jordan Canonical Form"
extraction_confidence: high
aliases: []
prerequisites:
  - jordan-canonical-form
extends: []
related:
  - eigenvalue
  - jordan-block
contrasts_with: []
answers_questions:
  - "What is a generalized eigenspace?"
---

# Quick Definition
The generalized eigenspace of T for eigenvalue $\lambda$ is $V_\lambda = \ker(T - \lambda I)^{n_\lambda}$ where $n_\lambda$ is the algebraic multiplicity of $\lambda$. When the characteristic polynomial splits, $V = \bigoplus_\lambda V_\lambda$.

# Core Definition
If $\lambda$ is an eigenvalue of T with algebraic multiplicity $n_\lambda$ (the power of $(x - \lambda)$ in the characteristic polynomial), the generalized eigenspace is $V_\lambda = \{v \in V \mid (T - \lambda I)^{n_\lambda}(v) = 0\}$. This corresponds to the direct sum of cyclic F[x]-modules with annihilator a power of $(x - \lambda)$. When the characteristic polynomial splits, $V = V_{\lambda_1} \oplus \cdots \oplus V_{\lambda_k}$ (Dummit & Foote, pp. 491-494).

# Prerequisites
- **jordan-canonical-form** — Generalized eigenspaces give the Jordan decomposition

# Key Properties
1. $\dim V_\lambda = $ algebraic multiplicity of $\lambda$
2. $\dim \ker(T - \lambda I) = $ geometric multiplicity = number of Jordan blocks for $\lambda$
3. $V = \bigoplus V_\lambda$ when char poly splits

# Relationships
## Builds Upon
- **jordan-canonical-form**

## Related
- **eigenvalue**, **jordan-block**

# Source Reference
Chapter 12, Section 12.3, pp. 491-494.

# Verification Notes
- Confidence: HIGH — standard definition in context of JCF
