import type { ComponentType } from "react";
import MainLayout from "../../../layouts/main.layout";
import Header from "../../../widgets/Header";
import Footer from "../../../widgets/Footer";
import Landing from "../../../pages/Landing";

export interface LayoutProps {
  children: React.ReactNode;
  header?: React.ReactNode;
  footer?: React.ReactNode;
}

export type AppRoute = {
  layout: ComponentType<LayoutProps>;
  header: ComponentType<unknown>;
  footer: ComponentType<unknown>;
  children: ComponentType;
  path: string;
  protected: boolean;
};

export const appRoutes: AppRoute[] = [
  {
    layout: MainLayout,
    header: Header,
    footer: Footer,
    children: Landing,
    path: "/",
    protected: false,
  },
];
