import EventPreview from "./components/EventPreview"

const Events = () => {
    return (
        <div className="w-full box-border pt-20 pb-20 pr-3 pl-3 bg-bg-light-grey flex justify-center">
            <div className="w-full max-w-[1200px] flex flex-col gap-20 justify-center items-center">
                <div className="flex flex-col gap-7 items-start w-full">
                    <span className="text-[1rem] font-bold text-accent-light">
                        МЕРОПРИЯТИЯ
                    </span>
                    <div className="flex justify-between items-center w-full">
                        <span className="text-5xl font-bold text-text-second">
                            Ближайшие <span className="accent-gradient-text">события</span>
                        </span>
                        <button className="cursor-pointer box-border pt-2 pb-2 pr-6 pl-6 rounded-xl border border-border-gray flex gap-4 transition-colors duration-200 hover:bg-bg-grey-transparent">
                            <span className="text-[1rem] text-text-second font-bold">
                                Все мероприятия
                            </span>
                            <span className="text-[1rem] text-text-second font-bold">
                                {`->`}
                            </span>
                        </button>
                    </div>
                </div>
                <div className="grid grid-cols-3 gap-6 w-full">
                    <EventPreview/>
                    <EventPreview/>
                    <EventPreview/>
                </div>
            </div>
        </div>
    )
}

export default Events