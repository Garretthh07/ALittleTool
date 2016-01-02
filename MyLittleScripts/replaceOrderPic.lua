#!/usr/bin/env lua5.1
--[[
--  Author: Shunfa Zhang
--  Date: 2016/1/2
--  Use Lib <luafilesystem>: https://keplerproject.github.io/luafilesystem/
--  Based on Lua 5.1
--  Install:
--      luarocks install luafilesystem
--  Needed:
--      * VS 2012 or other
--      * Add %PATH%\luarocks-2.2.3-win32\win32\lua5.1\bin to System Path
--      * cl.exe to System Path
--      * If luarocks doesn't work, Please run vcvars32.bat to have a try
--]]

local string = require "string"
local os = require "os"

local assert, type = assert, type
local sep = string.match(package.config, "[^\n]+")
local lfs = require "lfs"
print (lfs._VERSION)

testDir = ""

local function attrdir (path, doAction)
        for file in lfs.dir(path) do
                if file ~= "." and file ~= ".." then
                        local f = path .. sep .. file
                        print ("=>\t " .. f .. " <=")
                        local attr = lfs.attributes (f)
                        assert(type(attr) == "table")
                        if attr.mode == "directory" then
                                attrdir(f)
                        else
                                -- This is a file, you can do something
                                --[[
                                for name, value in pairs(attr) do
                                    print("====> file: name: %s, value: %s", name, value)
                                end
                                ]]
                                doAction(f)
                        end
                end
        end
end

local function copyFile (orgDir, targetDir, sourceName)
        local attr = lfs.attributes (actorTargetDirc)
        if attr == nil then
                local res, msg = lfs.mkdir(targetDir)
                if res == nil then
                        print ("make file error: ", msg)
                end
        end

        local sourceFile = orgDir .. sep .. sourceName
        local targetFile = targetDir .. sep .. sourceName
        local copyCmd = string.format("%s %s", sourceFile, targetFile)
        -- Use the OS cmd -> cp, you can use io.open to replace
        os.execute(string.format("cp %s", copyCmd))
end

local function removeFile (targetFile)
        local attr = lfs.attributes (actorTargetDirc)
        if attr.mode == "directory" then
                for file in lfs.dir(targetFile) do
                    if file ~= "." and file ~= ".." then
                            local f = targetFile .. sep .. file
                            local attr = lfs.attributes (f)
                            assert(type(attr) == "table")
                            if attr.mode == "directory" then
                                    removeFile(f)
                            else
                                    os.remove(f)
                            end
                    end
                end
                lfs.rmdir(targetFile)
        else
                os.remove(targetFile)
        end
end

local function renameFile (path, oldName, newName)
        local oldPath = path .. sep .. oldName
        local newPath = path .. sep .. newName
        os.rename(oldPath, newPath)
end

--copyFile(actorDir, actorTargetDirc, "A001.png")
--removeFile(actorTargetDirc)
--renameFile(actorTargetDirc, "A001.png", "B001.png")
-- Write some rule to get the file you want
