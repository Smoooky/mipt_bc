const MainLayout = ({
  header,
  footer,
  children,
}: {
  header?: React.ReactNode;
  footer?: React.ReactNode;
  children: React.ReactNode;
}) => {
  return (
    <div className="flex flex-col screen-width h-auto">
      {header}

      <div className="_container flex-1 flex flex-col items-center">{children}</div>

      {footer}
    </div>
  );
};

export default MainLayout;
