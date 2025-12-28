import type { AppRoute } from "./config/routes.config";
import PublicRoute from "./PublicRoute";

type RouteWrapperProps = {
  route: AppRoute;
};

const RouteWrapper = ({ route }: RouteWrapperProps) => {
  const Layout = route.layout;
  const Header = route.header;
  const Footer = route.footer;

  const content = route.protected ? null : (
    <PublicRoute>
      <route.children />
    </PublicRoute>
  );

  return (
    <>
      <Layout
        header={Header ? <Header /> : null}
        footer={Footer ? <Footer /> : null}
      >
        {content}
      </Layout>
    </>
  );
};

export default RouteWrapper;
