MODULE constants
!
! Module containing constants:
!         PI,TWOPI, the number of grid elements in each direction n%g,
!         the various bin # params,
!         and the vars for the filepaths.
!

    implicit none
    save

    integer, parameter :: nxg=100, nyg=100, nzg=900 !30um sc
    !integer, parameter :: nxg=100, nyg=100, nzg=800 !20um sc
    !integer, parameter :: nxg=100, nyg=100, nzg=750 !15um sc
    !integer, parameter :: nxg=100, nyg=100, nzg=700 !10um sc
    !integer, parameter :: nxg=100, nyg=100, nzg=600 !0um sc





    real,    parameter :: PI=4.*atan(1.), TWOPI=2.*PI, OFFSET=1.e-2*(2.*.5/nxg)
    real               :: xmax, ymax, zmax, v(3), costim, sintim, cospim, sinpim
    character(len=255) :: cwd, homedir, fileplace, resdir

end MODULE constants
