import nest from '@habit/eslint-config/nest';

export default [
  ...nest,
  {
    languageOptions: {
      // Must be set here: type-aware linting resolves tsconfig.json relative
      // to this file, not to the shared config package.
      parserOptions: { tsconfigRootDir: import.meta.dirname },
    },
  },
];
