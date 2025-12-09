const EventPreview = () => {
    return (
        <div className="rounded-xl border border-border-dark-grey bg-bg-element-dark-blue flex flex-col element-shadow group transition-transform duration-300 hover:-translate-y-3">
            <div className="w-full box-border p-6 flex flex-col gap-4">
                <div className="w-full flex justify-between items-start">
                    <div className="rounded-xl accent-gradient-only box-border p-3 aspect-square min-w-19">
                        <div className="text-2xl text-text-thirst font-bold text-center">
                            15
                        </div>
                        <div className="text-[0.9rem] font-light text-center">
                            ДЕК
                        </div>
                    </div>
                    <span className="rounded-xl bg-bg-element-blue pt-[3px] pb-[3px] pr-3 pl-3 text-[0.8rem] text-accent-light">
                        Питчинг
                    </span>
                </div>
                <div className="flex flex-col gap-2">
                    <span className="text-xl font-bold text-text-second transition-colors duration-200 group-hover:text-accent-light">
                        Startup Pitch Night
                    </span>
                    <span className="text-[0.95rem] text-text-third">
                        Презентация стартапов перед инвесторами и экспертами
                    </span>
                    <div className="flex flex-col">
                        <div className="flex gap-2 items-center">
                            <span className="text-xl text-accent-light">
                                O
                            </span>
                            <span className="text-[0.9rem] text-text-third">
                                19:00
                            </span>
                        </div>
                        <div className="flex gap-2 items-center">
                            <span className="text-xl text-accent-light">
                                Y
                            </span>
                            <span className="text-[0.9rem] text-text-third">
                                Главный корпус МФТИ
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <div className="w-full box-border pb-6 pt-6 pr-6 pl-6 flex justify-center items-center border-t border-t-border-dark-grey opacity-0 transition-opacity duration-200 group-hover:opacity-100">
                <button className="box-border pb-2 pt-2 w-full rounded-xl cursor-pointer transition-colors duration-200 hover:bg-bg-element-grey">
                    <span className="text-[1rem] font-bold text-text-second">
                        Зарегистрироваться
                    </span>
                </button>
            </div>
        </div>
    )
}

export default EventPreview