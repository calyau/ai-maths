---
concept: Cyclotomic Extension
slug: cyclotomic-extension
category: galois-theory
subcategory: cyclotomic
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 598
section: "14.5 Cyclotomic Extensions and Abelian Extensions over Q"
extraction_confidence: high
aliases:
  - "cyclotomic field"
prerequisites:
  - cyclotomic-polynomial
  - galois-extension
extends: []
related:
  - abelian-extension
  - kronecker-weber-theorem
contrasts_with: []
answers_questions:
  - "What is a cyclotomic extension?"
---

# Quick Definition
The nth cyclotomic extension $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is obtained by adjoining a primitive nth root of unity to $\mathbb{Q}$. It is an abelian Galois extension with $\text{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^{\times}$.

# Core Definition
The nth cyclotomic extension of $\mathbb{Q}$ is $\mathbb{Q}(\zeta_n)$ where $\zeta_n = e^{2\pi i/n}$ is a primitive nth root of unity. It is the splitting field of $x^n - 1$ (or equivalently $\Phi_n(x)$) over $\mathbb{Q}$. The extension is Galois with $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \phi(n)$ and $\text{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^{\times}$, where $\sigma_a(\zeta_n) = \zeta_n^a$ for $\gcd(a,n) = 1$ (Dummit & Foote, pp. 598-605).

# Prerequisites
- **cyclotomic-polynomial** — $\Phi_n(x)$ is the minimal polynomial
- **galois-extension** — Cyclotomic extensions are Galois

# Key Properties
1. $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \phi(n)$
2. $\text{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^{\times}$ (abelian!)
3. The automorphism $\sigma_a$ sends $\zeta_n \mapsto \zeta_n^a$
4. Intermediate fields correspond to subgroups of $(\mathbb{Z}/n\mathbb{Z})^{\times}$
5. $\mathbb{Q}(\zeta_n)$ contains $\mathbb{Q}(\sqrt{(-1)^{(p-1)/2} p})$ for odd prime p dividing n

# Relationships
## Builds Upon
- **cyclotomic-polynomial**, **galois-extension**

## Enables
- **abelian-extension** — Cyclotomic extensions are abelian
- **kronecker-weber-theorem** — Every abelian extension of $\mathbb{Q}$ is contained in a cyclotomic extension

# Source Reference
Chapter 14, Section 14.5, pp. 598-605.

# Verification Notes
- Confidence: HIGH — detailed development
