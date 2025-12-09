import Activities from "./ui/Activities/Activities";
import Cases from "./ui/Cases/Cases";
import Events from "./ui/Events/Events";
import Hero from "./ui/Hero/Hero";
import Joining from "./ui/Joining/Joining";
import Partners from "./ui/Partners/Partners";
import Values from "./ui/Values/Values";

const Landing = () => {
  return (
    <>
      <Hero />
      <Values />
      <Events />
      <Activities />
      <Cases />
      <Joining />
      <Partners />
    </>
  );
};

export default Landing;
