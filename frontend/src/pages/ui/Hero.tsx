import './Hero.css'
import bgNet from '../../assets/background/background-net.png';
import Sparkle from 'src/widgets/Sparkle/Sparkle';

const Hero = () => {
  return (
    <>
      <div 
        className="absolute w-screen h-screen hero-background -z-1" 
        style={{ 
            backgroundImage: `
                url(${bgNet})
                `, 
        }}
        />
      <div className='_sparkles absolute w-screen h-screen z-0 flex justify-center items-center'>
        <Sparkle size={100} duration={2.5} color='var(--color-accent-light)' x={'10%'} y={'5%'}/>
        <Sparkle size={100} duration={3} color='var(--color-border-blue)' x={'-10%'} y={'-5%'}/>
      </div>
      <div
        className="absolute w-screen z-1 h-screen opacity-100"
        style={{ 
            backgroundImage: `
                linear-gradient(to bottom, rgba(23, 42, 69, 0) 50%, var(--color-bg-dark) 100%)
                `, 
        }}
        />
      <div className="w-screen h-screen flex justify-center items-center relative z-2">
        <div className="flex flex-col gap-8 items-center max-w-[700px]">
            <div className="box-border pt-2 pb-2 pr-4 pl-4 border border-border-blue rounded-3xl">
                <ul>
                    <li className="relative pl-3 before:absolute before:left-0 before:top-1/2 before:-translate-y-1/2 before:w-2 before:h-2 before:bg-accent-light before:rounded-full text-text-third">
                        <span className="box-border pl-1">
                            Сообщество предпринимателей МФТИ
                        </span>
                    </li>
                </ul>
            </div>
            <div className="flex flex-col gap-8 items-center">
                <div className="text-8xl font-bold flex flex-col items-center">
                    <span className="text-text-second">
                        Бизнес Клуб
                    </span>
                    <span className="accent-gradient-text">
                        МФТИ
                    </span>
                </div>
                <div className="text-center">
                    <span className="text-xl text-text-third">
                        Объединяем амбициозных студентов, предпринимателей и экспертов <br/> для создания инновационных проектов и развития бизнес-навыков
                    </span>
                </div>
                <div className="flex items-center gap-4">
                    <button className="cursor-pointer pt-3 pb-3 pr-10 pl-10 rounded-xl accent-gradient transition-transform duration-200 hover:-translate-y-[0.125em]">
                        <span className="inline text-[1.2rem] font-bold">
                            {'Вступить в клуб ->'}
                        </span>
                    </button>
                    <button className="cursor-pointer box-border pt-3 pb-3 pr-10 pl-10 rounded-2xl border-2 border-accent-border transition-colors duration-200 hover:bg-[#275ea665]">
                        <span className="text-[1.2rem] font-bold text-text-second">
                            Узнать больше
                        </span>
                    </button>
                </div>
            </div>
            <div className="grid grid-cols-3 gap-8 max-w-2xl mx-auto">
                <div className="min-w-[120px] flex flex-col gap-2 items-center justity-center rounded-xl bg-bg-element-dark box-border pt-4 pb-4 pl-14 pr-14 border border-border-dark-grey">
                    <div className="text-2xl text-accent-light">
                        OOO
                    </div>
                    <span className="text-3xl font-bold text-text-second">
                        500+
                    </span>
                    <span className="text-[1rem] text-text-third">
                        Участников
                    </span>
                </div>
                <div className="min-w-[120px] flex flex-col gap-2 items-center justity-center rounded-xl bg-bg-element-dark box-border pt-4 pb-4 pl-14 pr-14 border border-border-dark-grey">
                    <div className="text-2xl text-accent-lightest">
                        ААА
                    </div>
                    <span className="text-3xl font-bold text-text-second">
                        50+
                    </span>
                    <span className="text-[1rem] text-text-third">
                        Стартапов
                    </span>
                </div>
                <div className="min-w-[120px] flex flex-col gap-2 items-center justity-center rounded-xl bg-bg-element-dark box-border pt-4 pb-4 pl-14 pr-14 border border-border-dark-grey">
                    <div className="text-2xl text-accent-light">
                        УУУ
                    </div>
                    <span className="text-3xl font-bold text-text-second">
                        100+
                    </span>
                    <span className="text-[1rem] text-text-third">
                        Мероприятий
                    </span>
                </div>
            </div>
        </div>
      </div>
    </>
  );
};

export default Hero;
