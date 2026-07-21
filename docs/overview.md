# Overview

`hello-sandbox` provides one function, `greet`, which builds a greeting string.

## What this is

A minimal greeting library for testing and automation experiments. It exports a single function that generates personalized greetings, with sensible defaults for empty or whitespace-only names. This project is deliberately trivial and serves as a stable target for CI/CD workflows and pull-request automation.

## Behaviour

- `greet()` with no argument greets `world`.
- `greet(name)` greets `name`.
- Surrounding whitespace is stripped; a name that is empty after stripping
  falls back to `world`.

## Non-goals

Localisation, formatting options, and anything resembling a feature.
