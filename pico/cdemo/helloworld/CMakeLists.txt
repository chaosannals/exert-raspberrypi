add_executable(helloworld)

target_sources(
    helloworld
    PRIVATE
    main.c
)

target_link_libraries(
    helloworld
    pico_stdlib
)

pico_add_extra_outputs(helloworld)
