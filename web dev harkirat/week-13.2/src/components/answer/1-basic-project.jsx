export default function SidebarClass1() {
    return <div className="flex h-screen">
        <div className="bg-red-200 w-0 sm:w-96 transition-all duration-1000">
            Sidebar
        </div>
        <div className="bg-green-200 w-full">
            Content
        </div>
    </div>;
}