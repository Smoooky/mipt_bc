import { defineConfig } from "eslint/config";

import tseslint from "@typescript-eslint/eslint-plugin";
import tsparser from "@typescript-eslint/parser";
import prettierPlugin from "eslint-plugin-prettier";
import prettierConfig from "eslint-config-prettier";
import pluginReact from "eslint-plugin-react";

export default defineConfig([
  { 
    files: ["**/*.{ts,tsx}"],
    plugins: {
      "@typescript-eslint": tseslint,
      prettier: prettierPlugin,
    },
    languageOptions: {
      parser: tsparser,
      sourceType: "module",
    },
    rules: {
      ...tseslint.configs.recommended.rules,
      ...prettierConfig.rules,
      "@typescript-eslint/no-unused-vars": "warn",
      "no-console": "warn",
      "semi": ["error", "always"],
      "quotes": ["error", "double"],
      "prettier/prettier": "error",
      'react/react-in-jsx-scope': 'off',
    },
  },
  prettierPlugin.configs.recommended,
  pluginReact.configs.flat['jsx-runtime'],
]);
