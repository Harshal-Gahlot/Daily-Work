interface User {
    id: string;
    name: string;
    age: string;
    email: string;
    password: string;
}

// use Pick to pick only few items from interface or type, by doin' so we still only hv 1 singe source of truth
type toUpdateUser = Pick<User, "name" | "age" | "email" | "password">;

// type given Partial will all be optional, i.e. ts will not throw error even if I don't provide it with one or all values. 
type toUpdateUserOptional = Partial<toUpdateUser>;
// it's similar to "?" operator except it's for custom types.

const displayUsers = (user: toUpdateUserOptional) => {
    console.log("user.name", user.name);
    console.log("user.email", user.email);
};

// no error:
displayUsers({
    name:"abc",
})