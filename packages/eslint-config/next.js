import nextVitals from 'eslint-config-next/core-web-vitals';
import nextTs from 'eslint-config-next/typescript';
import prettier from 'eslint-config-prettier/flat';
import { ignores, sharedRules } from './base.js';

/**
 * Next.js web app. Deliberately does NOT extend ./base.js — eslint-config-next
 * registers its own typescript-eslint setup, and layering a second one on top
 * duplicates plugin registration. The shared rules are applied directly instead.
 */
export default [{ ignores }, ...nextVitals, ...nextTs, { rules: sharedRules }, prettier];
